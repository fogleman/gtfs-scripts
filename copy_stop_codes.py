import gtfs
import sys

def copy_stop_codes(src_path, dst_path, out_path):
    src, _ = gtfs.read(src_path)
    dst, fieldnames = gtfs.read(dst_path)
    lookup = dict((x['stop_name'], x) for x in src)
    max_stop_code = 0
    for row in src:
        try:
            max_stop_code = max(max_stop_code, int(row['stop_code']))
        except Exception:
            pass
    for row in dst:
        stop_name = row['stop_name']
        if stop_name in lookup:
            stop = lookup[stop_name]
            row['stop_code'] = stop['stop_code']
        else:
            max_stop_code += 1
            row['stop_code'] = max_stop_code
            print 'WARNING: Could not find stop:', stop_name
    gtfs.write(out_path, dst, fieldnames)

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print 'Usage: python copy_stop_codes.py src.txt dst.txt out.txt'
        return
    copy_stop_codes(*args)

if __name__ == '__main__':
    main()
