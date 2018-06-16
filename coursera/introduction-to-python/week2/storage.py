#!/usr/bin/env python3
import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_args():
    parser = argparse.ArgumentParser(description='key-value storage')
    parser.add_argument('--key')
    parser.add_argument('--val')
    args = parser.parse_args()
    return vars(args)


def get_json_data(storage_path=storage_path):
    json_data = {}
    if os.path.exists(storage_path):
        with open(storage_path) as fh:
            try:
                json_data = json.load(fh)
            except json.decoder.JSONDecodeError as ex:
                pass
    return json_data


def main(args, storage_path=storage_path):
    json_data = get_json_data()
    if args['val']:
        # store
        value = json_data.get(args['key'], [])
        value.append(args['val'])
        json_data[args['key']] = value
        with open(storage_path, 'w') as fh:
            json.dump(json_data, fh)
    else:
        data = json_data.get(args['key'], [])
        print(', '.join(data))


if __name__ == '__main__':
    args = get_args()
    main(args)
