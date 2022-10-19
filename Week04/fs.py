import argparse
import os
import yaml
import re
from sre_constants import FAILURE

class C:
    """
    A class that defines the ASCII control characters to color the terminal
    """
    HEADER = '\033[95m'
    Yikes = '\033[94m'
    Boomer = '\033[96m'
    Forest = '\033[92m'
    WARN = '\033[93m'
    FAILURE = '\033[91m'
    ENDCODE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_files(directory):
    # check if the given argument is a directory
    if not os.path.isdir(directory):
        print(f"Invalid Directory => {directory}")
        exit()
    f_list = []
    # Crawl through the provided directory
    for root, subfolders, filenames in os.walk(directory):
        # loop through every file and add the root to it.
        for f in filenames:
            # file_list = directory + "\\" + f
            file_list = directory + "/" + f
            f_list.append(file_list)
    return f_list

def load_ruleset(ruleset):
    rules = []
    selected_ruleset = {}
    with open("rules.yaml", 'r') as f:
        try:
            # Load all of the books within the yaml file
            for rule in yaml.load_all(f, Loader=yaml.SafeLoader):
                # Append the rules
                rules.append(rule)
        # Catch a yaml error if their is one.
        except yaml.YAMLError as exc:
            print(exc)
    for rule in rules:
        try:
            if rule[ruleset]:
                selected_ruleset = rule
        except KeyError:
            continue
    # if the ruleset is validated return it
    if selected_ruleset:
        return selected_ruleset
    # if not tell the user they entered an invalid ruleset.
    else:
        print(f"Invalid Ruleset => {ruleset}")
        exit(0)
        return None

if __name__ == "__main__":
    # set up our arg parser
    parser = argparse.ArgumentParser(
        description="Searches a group of log files for threat indicators based on a given ruleset",
        epilog="Developed by Thomas Autiello 2022 02 10"
    )
    parser.add_argument("-d", "--directory", required=True, help="Directory with your logs.")
    parser.add_argument("-r", "--rules", required=True, help="Ruleset from rules.yaml that you would like to use.")
    args = parser.parse_args()
    # load the values of our arguments into their respective variables
    root_dir = args.directory
    rule_set = args.rules
    output_f = args.output
    files = load_files(root_dir)
    rules = load_ruleset(rule_set)
    rule_def = rules[rule_set]
    # create an empty list to store our output if it is going to be saved to a file
    file_output_list = []
    for file in files:
        with open(file, "r") as f:
            log_lines = f.readlines()
            for log_line in log_lines:
                for rule, definition in rule_def.items():
                    # search the file for out match
                    if re.search(definition, log_line):
                        # if output file is defined, save the match to our output list
                        if output_f:
                            match = f"Rule: {rule} Has been matched in Ruleset: {rule_set} Within File: {file}\n" \
                                    f"Matched Log Entry:{log_line}\n\n"
                            file_output_list.append(match)
                        # if no output is defined print the results to the console with color coding
                        else:
                            log_line = re.sub(definition, f"{C.FAILURE}{definition}{C.ENDCODE}", log_line)
                            print(f"{C.WARN}Rule: {C.FAILURE}{rule}{C.WARN} Has been matched in Ruleset: {C.WARN}"
                                  f"{rule_set} {C.WARN} Within File: {C.Boomer}{file}{C.ENDCODE}\n"
                                  f"{C.Yikes}Matched Log Entry:{C.ENDCODES} {log_line}\n\n")
    if output_f and match:
        with open(output_f, "w+") as f:
            for match in file_output_list:
                f.write(match)