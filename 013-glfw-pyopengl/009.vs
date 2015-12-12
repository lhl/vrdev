#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec2 texCoord;

out vec3 ourColor; // color output to fragment shader
out vec2 TexCoord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
  gl_Position = projection * view * model * vec4(position, 1.0);
  ourColor = color; // Set the color to the input color from the vertex data
  TexCoord = texCoord;
  // Reverse
  // TexCoord = vec2(texCoord.x, 1.0 - texCoord.y);
}
