from fivek import MITAboveFiveK
print('Jay Shree Krishna !!')
fivek_dataset = MITAboveFiveK(
    root="/media/iiserb/Elements/FiveK-Dataset",       # Path to store or find the dataset
    split="train",                    # Use the training split
    download=True,                    # Download if not present
    experts=["a", "b","c","d","e"]                # Load retouches from Expert A and B
)
# five_k = MITAboveFiveK(
#     root='/home/hari-krishna/Downloads/',
#     split='train'
#     download
