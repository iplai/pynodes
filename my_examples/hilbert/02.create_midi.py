import mido, math


def l_system(axiom, rules, generations):
    """
    Generate an L-system string.

    :param axiom: The starting string.
    :param rules: A dictionary of replacement rules.
    :param generations: The number of iterations to perform.
    :return: The final L-system string.
    """
    for i in range(generations):
        new_string = ""
        for char in axiom:
            if char in rules:
                new_string += rules[char]
            else:
                new_string += char
        axiom = new_string
    return axiom


def get_points(l_system_string, angle, distance):
    """
    Generate a list of points from an L-system string.

    :param l_system_string: The L-system string.
    :param angle: The angle to turn in degrees.
    :param distance: The distance to move forward.
    :return: A list of (x, y) tuples representing the points.
    """
    x = 0
    y = 0
    direction = 0
    points = [(x, y)]
    for char in l_system_string:
        if char == "F":
            x += distance * math.cos(math.radians(direction))
            y += distance * math.sin(math.radians(direction))
            points.append((round(x), round(y)))
        elif char == "+":
            direction += angle
        elif char == "-":
            direction -= angle
    return points


def get_corners(points):
    """
    Get the corner points from a list of points.

    :param points: A list of (x, y) tuples representing the points.
    :return: A list of (x, y) tuples representing the corner points.
    """
    corners = [points[0]]
    for i in range(1, len(points) - 1):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        x3, y3 = points[i + 1]
        if (x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2):
            corners.append((x2, y2))
    corners.append(points[-1])
    return corners


axiom = "+A"
rules = {
    'A': '-BF+AFA+FB-',
    'B': '+AF-BFB-FA+'
}
generations = 4
angle = 90
distance = 1

l_system_string = l_system(axiom, rules, generations)
points = get_points(l_system_string, angle, distance)
corners = get_corners(points)


def pitch_mapping_major_c(x: int, offset=0, min_pitch=60 - 12, max_pitch=60 + 12):
    # 0 -> 60 : center Do
    x = x + offset
    base = [60, 62, 64, 65, 67, 69, 71]
    result = math.floor(x / 7) * 12 + base[x % 7]
    while result < min_pitch:
        result += 12
    while result > max_pitch:
        result -= 12
    return result


bpm = 120
tempo = round(6e7 / bpm)
# time = 480 表示1拍
# 音高:21 -> 108, 音量:0 -> 127, 拍数
# notes = [(pitch, velocity, beats)]
notes = []
angle = 90
velocity = 64
for i in range(1, len(corners)):
    point1, point2 = corners[i - 1], corners[i]
    if point1[1] != point2[1]:
        continue
    notes.append((point1[1], velocity, abs(point1[0] - point2[0]) * 0.5))

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
track.append(mido.MetaMessage("set_tempo", tempo=tempo, time=0))
track.append(mido.MetaMessage("track_name", name="Piano 1", time=0))
track.append(mido.Message("program_change", program=1, time=0))  # 这个音轨使用的乐器

# 开头加一个1拍的休止符
# track.append(mido.Message("note_on", note=0, velocity=0, time=0))
# track.append(mido.Message("note_off", note=0, velocity=0, time=round(480 * 1)))

for note in notes:
    pitch, velocity, beats = note
    track.append(mido.Message("note_on", note=pitch_mapping_major_c(pitch), velocity=velocity, time=0))
    track.append(mido.Message("note_off", note=pitch_mapping_major_c(pitch), velocity=velocity, time=round(480 * beats)))
mid.save("my_examples/hilbert/hilbert.midi")
