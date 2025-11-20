import subprocess
import sys
import os


def run_tests():
    # Добавляем текущую директорию в PYTHONPATH
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, 'src')

    browsers = ["chrome", "firefox"]

    for browser in browsers:
        print(f"\n{'=' * 50}")
        print(f"Running tests in {browser}")
        print(f"{'='=
        50}")

        cmd = [
            "pytest",
            os.path.join(src_dir, "tests"),
            f"--browser={browser}",
            "--alluredir=allure-results",
            "-v",
            "-s"
        ]

        # Устанавливаем PYTHONPATH
        env = os.environ.copy()
        env['PYTHONPATH'] = src_dir

        result = subprocess.run(cmd, env=env)

        if result.returncode != 0:
            print(f"Tests failed in {browser}")
            # Не выходим сразу, продолжаем с другим браузером


if __name__ == "__main__":
    run_tests()