from datasets import load_dataset

# 从本地文件加载数据集
squad_it_dataset = load_dataset("json", data_files="SQuAD_it-train.json", field="data")

data_files = {"train": "SQuAD_it-train.json", "test": "SQuAD_it-test.json"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")

# Datasets实际上支持输入文件的自动解压,所以我们可以跳过使用gzip,直接设置 data_files参数传递压缩文件:
data_files = {"train": "SQuAD_it-train.json.gz", "test": "SQuAD_it-test.json.gz"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")

# 从远程文件加载数据集
url = "https://github.com/crux82/squad-it/raw/master/"
data_files = {
    "train": url + "SQuAD_it-train.json.gz",
    "test": url + "SQuAD_it-test.json.gz",
}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")