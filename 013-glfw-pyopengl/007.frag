#version 330

in vec3 ourColor;
in vec2 TexCoord;

out vec4 color;

uniform sampler2D ourTexture;

void main()
{
  // Original
  // color = texture(ourTexture, TexCoord);

  vec2 uv = TexCoord;

  // uv.x = sqrt( (0.5 * 0.5) - ((uv.x-0.5)*(uv.x-0.5)) );
  // color = texture(ourTexture, uv);

  float tech_DistortionFactor = 0.2;
  // uv.x += tech_DistortionFactor * (-2.0 * uv.x + 1.0) * uv.x * (uv.x);
  uv.y += tech_DistortionFactor * (-2.0 * uv.y + 1.0) * uv.x * (uv.x - 1.0);
  color = texture(ourTexture, uv);

  /*
  float dist = distance(uv, vec2(0,0));
  float radius = 0.5;
  if ( abs (dist - radius) < thickness) {
    color=vec4(1.0, 0.0, 0.0, 1.0); 
  } else {
    color=vec4(0.0, 0.0, 1.0, 1.0); 
  }
  */




  // http://www.sudoplaygames.com/blog/2014/10/02/how-to-a-simple-curved-gui.html
  /*
  float tech_DistortionFactor = 0.2;
  vec2 uv = TexCoord;
  uv.y += tech_DistortionFactor * (-2.0 * uv.y + 1.0) * uv.x * (uv.x - 1.0);
  color = texture(ourTexture, uv);
  */


  // http://www.geeks3d.com/20130705/shader-library-circle-disc-fake-sphere-in-glsl-opengl-glslhacker/4/
  /*
  vec2 p = -1.0 + 2.0 * TexCoord;
  float r = 0.8*sqrt(dot(p,p));
  if(r<1.0) {
    vec2 uv;

    // sqrt(1-(x-1)^2)

    float f = (1.0-sqrt(1.0-r))/(r);
    uv.x = p.x*f + 0.5;
    uv.y = p.y*f + 0.5;
    color = texture(ourTexture, uv);
  } else {
    // Transparent
    color = vec4(0.0, 0.0, 0.0, 0.0);
  }	
  */
}
