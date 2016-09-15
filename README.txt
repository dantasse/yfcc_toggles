Ok, take in the YFCC100M dataset, and tell how many times people toggle between geotagging and not.

    shrink_yfcc100m.py --input_file=(yfcc100m_dataset)
--output_file=small_yfcc.csv
    sort small_yfcc.csv > small_yfcc_sorted.csv # (takes a while, use
screen/tmux)
    count_toggles.py --input_file=small_yfcc_sorted.csv
