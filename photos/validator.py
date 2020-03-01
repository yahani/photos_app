from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def photo_validator(image):
    image_width, image_height = get_image_dimensions(image)
    file_size = image.size
    if image_width >= 4000 or image_height >= 4000:
        raise ValidationError('Maximum dimensions allowed is 4000px X 4000px')
    if file_size > 3145728:
        raise ValidationError("Maximum file size allowed is 3MB")
