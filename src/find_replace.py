import os
import sys
import fileinput

# file to search
fileToSearch = "lib.rs"
#fileToSearch = "challenge.rs"

# text to search
textToSearch = [
    "event_loop::{ControlFlow, EventLoop},",
    "window::{Window, WindowBuilder},",
    "struct State {",
    "wgpu::Surface,",
    "window: Window,",
    "impl State {",
    "async fn new(window: Window) -> Self {",
    "let surface = unsafe { instance.create_surface(&window) }.unwrap();",
    "features: wgpu::Features::empty(),",
    "limits: wgpu::Limits::default(),",
    "view_formats: vec![],",
    "virtual_keycode: Some(VirtualKeyCode::Space),",
    "self.use_complex = *state == ElementState::Pressed;",
    "let event_loop = EventLoop::new();",
    "let mut state = State::new(window).await;",
    "event_loop.run(move |event, _, control_flow| {",
    "input:",
    "KeyboardInput {",
    "virtual_keycode: Some(VirtualKeyCode::Escape),",
    "} => *control_flow = ControlFlow::Exit,",
    "Event::RedrawRequested(window_id) if window_id == state.window().id() => {",
    "WindowEvent::Resized(physical_size) => {",
    "WindowEvent::ScaleFactorChanged { new_inner_size, .. } => {",
    "state.resize(**new_inner_size);"
]

# new text to replace
textToReplace = [
    "event_loop::EventLoop,",
    "window::{Window, WindowBuilder}, keyboard::{PhysicalKey, KeyCode},",
    "struct State<'a> {",
    "wgpu::Surface<\'a>,",
    "window: &'a Window,",
    "impl<'a> State<'a> {",
    "async fn new(window: &'a Window) -> State<'a> {",
    "let surface = instance.create_surface(window).unwrap();",
    "required_features: wgpu::Features::empty(),",
    "required_limits: wgpu::Limits::default(),",
    "desired_maximum_frame_latency: 2, view_formats: vec![],",
    "physical_key: PhysicalKey::Code(KeyCode::Space),",
    "self.use_color = false;",
    "let event_loop = EventLoop::new().unwrap();",
    "let mut state = State::new(&window).await;",
    "event_loop.run(move |event, control_flow| {",
    "event:",
    "KeyEvent {",
    "physical_key: PhysicalKey::Code(KeyCode::Escape),",
    "} => control_flow.exit(),",
    "WindowEvent::RedrawRequested => {",
    "WindowEvent::Resized(physical_size) => {",
    "//WindowEvent::ScaleFactorChanged { new_inner_size, .. } => {",
    "//state.resize(**new_inner_size);"
]

# number of items in array
textItems = len(textToSearch)

tempFile = open(fileToSearch, 'r+')

for line in fileinput.input(fileToSearch):
    for item in range(textItems):
        if textToSearch[item] in line:
            # once a item is found break the inner loop
            print("change item: " + str(item))
            break
    # replace text
    tempFile.write(line.replace(textToSearch[item], textToReplace[item]))

tempFile.close()

print('finished..')
