import unittest

from djangix.utils.geo import calc_distance


class Test(unittest.TestCase):
    test_cases = (
        (52.2296756, 21.0122287, 41.8919300, 12.5113300, 1315880),  # Варшава, Польша до Рима, Италия
        (34.052235, -118.243683, 40.712776, -74.005974, 3936854),   # Лос-Анджелес, США до Нью-Йорка, США
        (51.507351, -0.127758, 48.856613, 2.352222, 343646),        # Лондон, Великобритания до Парижа, Франция
        (55.755825, 37.617298, 59.934280, 30.335099, 633194),       # Москва, Россия до Санкт-Петербурга, Россия
        (35.689487, 139.691706, 37.774929, -122.419418, 8273041),   # Токио, Япония до Сан-Франциско, США
        (48.856613, 2.352222, 52.520008, 13.404954, 877705),        # Париж, Франция до Берлина, Германия
        (39.904202, 116.407394, 31.230416, 121.473701, 1067609),    # Пекин, Китай до Шанхая, Китай
        (55.676098, 12.568337, 59.329323, 18.068581, 522276),       # Копенгаген, Дания до Стокгольма, Швеция
    )

    def test_calc_distance(self):
        for first_lat, first_long, second_lat, second_long, expected_distance in self.test_cases:
            with self.subTest(lat1=first_lat, long1=first_long, lat2=second_lat, long2=second_long):
                calculated_distance = calc_distance(first_lat, first_long, second_lat, second_long)
                self.assertAlmostEqual(
                    first=calculated_distance,
                    second=expected_distance,
                    delta=10.0  # Используем delta для допуска / погрешности
                )


if __name__ == "__main__":
    unittest.main()
