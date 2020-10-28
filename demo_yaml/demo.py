import yaml


def reade_yaml():
    with open("./test.yaml", encoding="utf-8")as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)


if __name__ == '__main__':
    reade_yaml()
