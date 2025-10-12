words: dict[str, int] = {}


uInput = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam volutpat odio augue, at placerat odio fringilla sed. Cras ac quam quis elit aliquam fringilla. Pellentesque posuere luctus dolor, sit amet sollicitudin purus faucibus at. Fusce pulvinar sed mi ut gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras ultrices tellus vel luctus tincidunt. In a lectus enim. Nulla lobortis neque id dapibus aliquet. Phasellus pharetra nisi dui, ac vehicula diam rutrum ac. Mauris pulvinar rutrum fringilla. Ut aliquam libero et nulla pulvinar, sit amet tempor dolor viverra. Pellentesque consequat tempor eros, cursus rhoncus dui pellentesque ac. In ultrices tortor sed metus imperdiet, sed fringilla massa tempus.
Vestibulum dignissim condimentum commodo. Mauris non risus lectus. Etiam blandit ante turpis, eget fringilla turpis ultrices sit amet. Duis pellentesque semper semper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur efficitur ipsum quis neque porttitor, feugiat cursus velit facilisis. Praesent fermentum nisi eget facilisis consequat. Etiam purus augue, luctus nec suscipit nec, lobortis in odio. Ut a metus orci. Sed id ligula ut velit iaculis dignissim nec at mauris. Proin tristique, turpis vitae laoreet venenatis, sem diam suscipit tellus, ac efficitur purus justo ac metus. Sed sagittis nec urna in ultrices. Fusce pulvinar risus tortor, id malesuada tortor placerat id. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
Donec volutpat, libero vitae mattis dapibus, tellus orci blandit leo, vel sagittis odio orci consequat turpis. Donec in suscipit felis. Fusce in neque sodales, vestibulum ipsum sed, aliquam tellus. In varius ultricies ultrices. Donec purus arcu, condimentum eu maximus convallis, imperdiet ac tortor. Vivamus nec velit massa. Nunc pharetra tellus sit amet pulvinar imperdiet. Cras mollis consequat varius. Proin ultrices quam in nisi convallis, et sagittis orci tincidunt. Vestibulum ornare dictum arcu.'''

noDots = ''.join(uInput.split('.'))
noCommas = ''.join(noDots.split(','))
noNothing = noCommas.split(' ')

for string in noNothing:
    try:
        words[string.upper()] += 1
    except KeyError:
        words[string.upper()] = 1

for key, value in words.items():
    print(f'Palavra: {key:14}, Quantidade: {value:3}')