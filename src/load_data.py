# Read the data from the source and  save it to the data\raw path

import os
from get_data import get_data, read_params
import argparse


def load_and_save(config_path):
    config = read_params(config_path)
    data = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in data.columns]
    # print(new_cols)
    raw_data_path = config["load_data"]['raw_dataset_csv']
    data.to_csv(raw_data_path, sep=",", index=False, header=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_arg = args.parse_args()
    load_and_save(config_path=parsed_arg.config)
