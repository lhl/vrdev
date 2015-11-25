#version 330

layout (location = 0) in vec3 position; // position variable attribute position 0
layout (location = 1) in vec3 color;    // color variable has attribute position 0

out vec3 ourColor; // color output to fragment shader

void main()
{
  gl_Position = vec4(position, 1.0);
  ourColor = color; // Set the color to the input color from the vertex data
}
