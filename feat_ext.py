import subprocess
import sys
import argparse
import os
import multiprocessing as mp

import create_unique_list
import create_vectors

from tqdm import tqdm


def run_command(cmd):
    output = subprocess.run(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, universal_newlines=True)

    return [output.returncode, output.stdout]


def get_manifest(apk_path):
    cmd = ["aapt", "d", "xmltree", apk_path, "AndroidManifest.xml"]
    return run_command(cmd)


def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def main():

    parser = argparse.ArgumentParser(description='Feature extraction')
    parser.add_argument('-i', '--input', help='Input folder', required=True)
    # parser.add_argument('-o', '--output', help='Output csv', required=True)
    parser.add_argument('-e', '--extract',
                        help='Folder to extract apk to', required=True)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    apk_foler = args.input
    output_csv = args.output
    extract_folder = args.extract
    files = os.listdir(apk_foler)

    count_extracted = 0
    count_failed = 0
    fails = []

    print("Step 1: Getting manifest")
    for file in tqdm(files):
        if file.endswith(".apk"):
            apk_path = os.path.join(apk_foler, file)
            apk_name = file[:-4]
            ret, output = get_manifest(apk_path)
            if ret == 0:
                count_extracted += 1
                write_to_file(os.path.join(
                    extract_folder, apk_name + ".txt"), output)
                # run_command(
                #     ["./capture_feat.sh", extract_folder + '/' + apk_name + ".txt"])
            else:
                count_failed += 1
                fails.append(file)
                continue

    for fail in fails:
        files.remove(fail)

    print("Step 2: Extracting features")
    for file in tqdm(files):
        apk_name = file[:-4]
        run_command(
            ["./capture_feat.sh", extract_folder + '/' + apk_name + ".txt"])
        os.remove(extract_folder + '/' + apk_name + ".txt")

    with open('./1_List_Permissions.csv', 'w') as fp:
        pass

    with open('./2_List_Services.csv', 'w') as fp:
        pass

    with open('./3_List_Actions.csv', 'w') as fp:
        pass

    with open('./4_List_Categories.csv', 'w') as fp:
        pass

    print("Step 3: Creating unique list")
    for file in tqdm(files):
        apk_name = file[:-4]
        create_unique_list.func(extract_folder + '/' +
                                apk_name + "_features.txt")

    print("Step 4: Creating csv")

    for file in tqdm(files):
        apk_name = file[:-4]
        create_vectors.csv_gen(extract_folder + '/' +
                               apk_name + "_features.txt", extract_folder)

    print("Extracted: " + str(count_extracted))
    print("Failed: " + str(count_failed))


if __name__ == '__main__':
    main()
