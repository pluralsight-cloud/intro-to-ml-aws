# Additional Code Snippets

This documents some of the additional custom code that was written for the lecture `Demo: Building a Custom Image Classification Model with SageMaker JumpStart`.

## Updated Query Code

This code is used in the cell under the heading `Query endpoint that you have created with the opened images and parse predictions`.

```python
for filename, img in images.items():
    query_response = query_endpoint(img)
    predicted_label, probabilities, labels = parse_prediction(query_response)
    display(HTML(f'<img src={filename} alt={filename} align ="left" style="width: 250px;"/>'
                 f'<figcaption>Predicted Label is : cat {probabilities[0]}, dog {probabilities[1]}'))
```

**Only the last line has changed**, to provide the probabilities for each label, rather than just the `predicted_label`.

## Adding additional images

After uploading the image to the working directory in your SageMaker Studio, add the following line to the cell under the heading beginning with: `Open the downloaded images and load in memory`.

```python
with open('custom-image.jpg', 'rb') as file: images['custom-image.jpg'] = file.read()
```

Once the cell has been executed, the image will be added to the `images` dictionary. Next time you run an inference, it will also run the inferences against any other images that you upload as well.