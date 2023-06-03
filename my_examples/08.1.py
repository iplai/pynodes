import bpy, math

bpy.ops.outliner.orphans_purge(do_recursive=True)


def prime_fast_generator(n):
    result = [2, 3]
    a = 5
    b = 7
    count = 3
    factor = [5]  # caching factor
    threshold = 25  # instead of calculating square-root on each candidate,
    while a < n:  # ...I change threshold every other time
        if a == threshold:
            factor.append(result[count])
            threshold = factor[-1]**2
            count += 1
        elif all(a % k for k in factor):
            result.append(a)
        if b >= n:
            break
        elif b == threshold:
            factor.append(result[count])
            threshold = factor[-1]**2
            count += 1
        elif all(b % k for k in factor):
            result.append(b)
        a += 6
        b += 6
    return result


primes = prime_fast_generator(100000)
n = len(primes)
print(n)

curve_data = bpy.data.curves.new("Prime Curve", "CURVE")
curve_obj = bpy.data.objects.new("Prime Curve", curve_data)
curve_spline = curve_data.splines.new('NURBS')  # 'POLY' 'BEZIER' 'BSPLINE' 'CARDINAL' 'NURBS'
curve_spline.points.add(n - 1)
for i in range(n):
    prime = primes[i]
    curve_spline.points[i].co = prime * math.cos(prime), prime * math.sin(prime), 0, 1
bpy.context.collection.objects.link(curve_obj)
