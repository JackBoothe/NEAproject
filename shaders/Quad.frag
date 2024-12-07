#version 330 core

layout (location = 0) out vec4 fragColor;

in vec3 color;
in vec4 frag_position;

void main(){
    float depth = frag_position.z / frag_position.w;

    // Output the depth as grayscale color
    fragColor = vec4(vec3(depth), 1.0);
}