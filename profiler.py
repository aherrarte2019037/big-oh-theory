import cProfile
import pstats
import io

def profile_function(func):
    pr = cProfile.Profile()
    pr.enable()

    func()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.strip_dirs().sort_stats('cumulative').print_stats()

    output = s.getvalue()
    output = output.replace('seconds', 'milliseconds')

    lines = output.split('\n')
    for i, line in enumerate(lines):
        if "percall" in line and "cumtime" in line:
            continue
        parts = line.split()
        if len(parts) >= 5:
            try:
                parts[2] = str(float(parts[2]) * 1000)
                parts[4] = str(float(parts[4]) * 1000)
                lines[i] = " ".join(parts)
            except ValueError:
                pass

    output = "\n".join(lines)
    print(output)
