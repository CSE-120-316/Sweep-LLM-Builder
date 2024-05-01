# import os
# import json
# from transformers import AutoTokenizer, AutoModel

# def convert_hf_to_json(model_name_or_path, output_dir):
#     # Load tokenizer and model
#     tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
#     model = AutoModel.from_pretrained(model_name_or_path)

#     # Create output directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Save tokenizer config as JSON
#     tokenizer_config = tokenizer.config.to_dict()
#     with open(os.path.join(output_dir, 'tokenizer_config.json'), 'w') as f:
#         json.dump(tokenizer_config, f, indent=4)

#     # Save model config as JSON
#     model_config = model.config.to_dict()
#     with open(os.path.join(output_dir, 'model_config.json'), 'w') as f:
#         json.dump(model_config, f, indent=4)

#     # Save model weights as separate JSON files
#     for name, tensor in model.state_dict().items():
#         json_path = os.path.join(output_dir, f'{name}.json')
#         with open(json_path, 'w') as f:
#             json.dump(tensor.tolist(), f)

#     print("Conversion completed successfully!")

# # Example usage
# model_name_or_path = "bert-base-uncased"
# output_dir = "/path/to/output_directory"

# convert_hf_to_json(model_name_or_path, output_dir)
