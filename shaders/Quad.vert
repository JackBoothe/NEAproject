#version 330 core

layout (location = 0) in vec3 in_position; //attributes for the vertex shader associated with location 0 meaning the vertex positions are expected to be bound to attribute location 0.
layout (location = 1) in vec3 in_color;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;


out vec3 color; //holds the colours associated with the vertex, passed to fragment shader
out vec4 frag_position;

void main(){
    mat4 mvp = m_proj * m_view * m_model;

    vec4 world_position = vec4(in_position, 1.0);
    vec4 clip_position = mvp * world_position;

     // Output the transformed position for further processing in the fragment shader
    frag_position = clip_position;

    // Output the final position (in homogeneous coordinates)
    gl_Position = clip_position;



}