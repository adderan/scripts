import sys

def main():
    for line in sys.stdin:
        info = line.split()
        if len(info) != 9:
            continue
        chrom, source, elementType, start, end, score, strand, a, group = info
        if "_" in chrom:
            continue
        if int(end) - int(start) > 10000:
            continue
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (chrom, source, elementType, start, end, score, strand, a, group))

if __name__ == "__main__":
    main()
