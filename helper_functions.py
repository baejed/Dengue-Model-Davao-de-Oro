def main():
    "hello"

if __name__ == "__main__":
    main()

def transform_classifications(transform_data):
    labels = transform_data.unique()
    values = range(len(labels))
    labels_dict = {label: val for label, val in zip(labels, values)}
    transformed_list = [labels_dict.get(data) for data in transform_data]
    return transformed_list, labels_dict

def transform_elevation(transform_data):
    elevation_dict = {"Low": 0, "Moderate": 1, "High": 2, "Higher": 3}
    transformed_list = [elevation_dict.get(data) for data in transform_data]
    return transformed_list, elevation_dict