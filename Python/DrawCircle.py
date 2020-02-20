def draw_circle(a: int, b: int, r: int) -> None:
    grid = [[' '] * (a + r + 1) for _ in range(b + r + 1)]
    
    def draw_point(x: int, y: int) -> None:
        grid[y][x] = '#'
            
    r_squared = r**2
    
    for x in range(r + 1):
        y = round((r_squared - x**2)**0.5)
        
        draw_point(a + x, b + y)
        draw_point(a + y, b + x)
        draw_point(a + x, b - y)
        draw_point(a + y, b - x)
        draw_point(a - x, b + y)
        draw_point(a - y, b + x)
        draw_point(a - x, b - y)
        draw_point(a - y, b - x)
        
    for row in grid:
        print(''.join(row))

draw_circle(5, 5, 5)