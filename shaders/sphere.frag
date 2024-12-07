#version 330 core

layout (location = 0) out vec4 fragColor;

in vec3 color;
in vec4 frag_position;

void main(){

    float ambientStrength = 0.1;

    //float depth = frag_position.x/ frag_position.z;
    // Output the depth as grayscale color
    fragColor = vec4(color , 1.0);
}