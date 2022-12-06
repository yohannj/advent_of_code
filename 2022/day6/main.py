#!/usr/bin/python3

def read_file(filename):
    with open(filename) as f:
        return f.read().strip('\n')

def find_start_of_packet_marker(buffer):
  # Keep track of the last four characters we've seen
  last_four = []

  # Iterate through the buffer one character at a time
  for i, c in enumerate(buffer):
    # Add the current character to the list of last four characters
    last_four.append(c)

    # If the list of last four characters is longer than four, remove the oldest character
    if len(last_four) > 4:
      last_four.pop(0)

    # If the last four characters are all different, return the number of characters processed so far
    if len(set(last_four)) == 4:
      return i + 1

# Test the function with the example inputs
print(find_start_of_packet_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))  # 7
print(find_start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'))  # 5
print(find_start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg'))  # 6
print(find_start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))  # 10
print(find_start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))  # 11

def find_end_of_packet_marker(signal: str, pattern_length: int):
    result = None
    idx = 0
    while not result and idx+pattern_length < len(signal):
        if len(set(signal[idx:idx+pattern_length])) == pattern_length:
            result = idx + pattern_length
        idx += 1

    return result

def part1():
    signal = read_file('input.txt')
    print(
        find_end_of_packet_marker(signal, 4)
    )

def part2():
    signal = read_file('input.txt')
    print(
        find_end_of_packet_marker(signal, 14)
    )

part1()
part2()
