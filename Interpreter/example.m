x = 0;
y = 1;

for x = 1:4 {
    print x, x+y;
}

while (x < 9) {
    print "HAHA" * x;
    x += 1;
}

for x = 1:10 {
    for y = 10:20{
        print x, y;
        break;
        y += 1;
    }
}

z = x + y;
print z, x, y;

a = eye(3);
b = zeros(5);
c = ones(9);
print a;
print b;
print c;
var = c[3];
var2 = a[1,1];
var3 = a[2,1];
print var, var2, var3;

