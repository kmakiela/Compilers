x = 0;
y = 1;
i = 0;

for x = 1:4 {
    print x, x+y;
}

while (x < 9) {
    print "( ͡° ͜ʖ ͡°) " * x;
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
i = 0;

print amIGlobal;
for i=1:5{
    amIGlobal = i;
    print amIGlobal;
}
print AmIGlobal;

ar1 = eye(3);
ar2 = eye(3);
ar1[1, 2] = 5;
ar1[2, 1] = 3;
ar3 = ar1 .+ ar2;
ar4 = ar1 .- ar2;
ar5 = ar1 .* ar2;

print ar3;
print ar4;
print ar5;