def blur_image(image, radius):
  """Blurs an image by `radius` pixels.

  Args:
    image: A 2-dimensional matrix of integers representing a black and white image.
    radius: The radius of the blur.

  Returns:
    A new image that has been blurred by `radius` pixels.
  """

  blurred_image = np.zeros_like(image)
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      neighbors = []
      for di in range(-radius, radius + 1):
        for dj in range(-radius, radius + 1):
          if 0 <= i + di < image.shape[0] and 0 <= j + dj < image.shape[1]:
            neighbors.append(image[i + di, j + dj])
      blurred_image[i, j] = np.mean(neighbors)
  return blurred_image


