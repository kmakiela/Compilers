
x = 0;
y = zeros(5);
z = x + y;

x = eye(5);
y = eye(8);
z = x + y;

x = [ 1,2,3,4,5 ];
y = [ [1,2,3,4,5],
      [1,2,3,4,5 ]];
z = x + y;

x = zeros(5);
y = zeros(7);
z = x + y;

x = ones(5);
z = x[4, 3];
z = x[78, 98];