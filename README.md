# game-controller
This is python based game controller, which can play mouse and click using color objects.
<br>
[![Documentation Status](https://readthedocs.org/projects/fairscale/badge/?version=latest)](https://fairscale.readthedocs.io/en/latest/?badge=latest) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/facebookresearch/fairscale/blob/master/CONTRIBUTING.md)
<br>
<br>
![output](result/output.gif)

## How does that work?
* Idea is to find colour for two objects, one for moving mouse another for clicking it. 
* Calculate external countours of both colored objects and use them to trigger mouse activity.
* `simple enough!!`
 

| File | Info |
|-----------|--------------|
| `main.py` | To choose color |
| `game.py` | Game python file |


### What color and how to choose it?
* So `main.py` is the file where you can place object in front of you and choose color parameters according to you!
* After calculating color values of both colored objects, use the value in `game.py`.

### well, where to use value in game.py?
* In `game.py`, you will get
```bash
lower_pink = np.array([139, 65, 121])
upper_pink = np.array([164, 88, 176])

lower_yellow = np.array([16, 101, 146])
upper_yellow = np.array([179, 255, 255])
```
* Change these values with your color values.
* So important thing is i have used `yellow` color to control the mouse and `pink` to fire clicks.
* Change your `yellow and pink` accordingly.

