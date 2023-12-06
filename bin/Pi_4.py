import os
import sys 
import argparse


class CustomHelpFormatter(argparse.HelpFormatter):
    def format_help(self):
        help_text = super().format_help()
        description = """
        Sorted intergenic spaces results as cp genome order.
        Author: Xu wenbo
        Org:    China Pharmaceutical University
        Email:  xwb7533@163.com"""
        return f"{description}\n\n{help_text}"


def sort_as_cp_order(input_file1, input_file2):
    pi_results = open(input_file1, 'r')
    cp_order_results = open(input_file2, 'r')
    results_file_path = os.path.join(os.path.dirname(input_file1), 'IGS_sort_as_cp_order.txt')
    reuslts_file = open(results_file_path, 'w')
    file1_line_list = pi_results.readlines()
    file2_line_list = cp_order_results.readlines()
    for IGS2 in file2_line_list:
        for IGS1 in file1_line_list:
            if IGS1.split('\t')[0] == IGS2.strip():
                print(IGS1, end='')
                reuslts_file.write(IGS1)
    reuslts_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter)
    parser.add_argument('-i', '--input', type=str, help="Input the file path of 'Pi_results.txt', generated by 06_Pi_3.py")
    parser.add_argument('-r', '--reference', type=str, help="Input the file path of 'cp_sort_IGS.txt', generated by 06_Pi_3.py")
    args = parser.parse_args()
    print(args)
    if not (args.input and args.reference):
        parser.print_help()
        sys.exit()
    else:
        sort_as_cp_order(args.input, args.reference)
        work_dir = os.path.dirname(args.input)
        final_path = os.path.abspath(os.path.join(work_dir, "IGS_sort_as_cp_order.txt"))
        print(f"The sorted results have been written into:\n"
            f"\t\t\t{final_path}")


