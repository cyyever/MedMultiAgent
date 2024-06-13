import logo from './logo.svg';
import './App.css';
import { ProChat } from '@ant-design/pro-chat';
import { useTheme } from 'antd-style';

import React, { useState, useEffect } from 'react';
import {
  AppstoreOutlined,
  HomeOutlined,
  CloudOutlined,
  HistoryOutlined,
  TeamOutlined,
  UploadOutlined,
  UserOutlined,
  VideoCameraOutlined,
} from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { Layout, Menu, theme, Typography, Divider  } from 'antd';


const { Header, Content, Footer, Sider } = Layout;

const { Title } = Typography;

type MenuItem = Required<MenuProps>['items'][number];

const items: MenuItem[] = [
  {
    label: 'Home',
    key: 'home',
    icon: <HomeOutlined />,
  },
  {
    label: 'History',
    key: 'history',
    icon: <HistoryOutlined />
  }
];

function App() {

  const {
    token: { colorBgContainer, borderRadiusLG, colorBgLayout, colorWhite },
  } = theme.useToken();

  const [currentTime, setCurrentTime] = useState(0);

  return (
    <div className="App">
      <Layout hasSider style={{ minHeight: '100vh' }}>
        <Sider
          style={{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0, top: 0, bottom: 0 }}
        >
          <Title level={3} style={{ color: colorWhite }}>MedMultiAgent</Title>
          <Divider style={{borderColor: colorWhite, width: 'calc(100% - 20px)' }} />
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['home']} items={items} />
        </Sider>
        <Layout style={{ marginLeft: 200 }}>
          <Header style={{ padding: 0, background: colorBgLayout }}>
            <Title level={3}>LLaMA-Med-Agent</Title>
          </Header>
          <Content style={{ margin: '24px 0px 0', overflow: 'initial' }}>
            <div
              style={{
                padding: 24,
                textAlign: 'center',
                background: colorBgContainer,
                borderRadius: borderRadiusLG,
              }}
            >
              <div style={{ backgroundColor: colorBgLayout, height: '80vh' }}>
                <ProChat
                  helloMessage={
                    'Welcome using MedMultiAgent. Feel free to ask anything'
                  }
                  // request={async (messages) => {
                  //   // const mockedData: string = `这是一段模拟的对话数据。本次会话传入了${messages.length}条消息`;
                  //   // return new Response(mockedData);

                  //   const response = await fetch('/stream-sse');
                  //   console.log('messages', messages);

                  //   if (!response.ok || !response.body) {
                  //     throw new Error(`HTTP error! status: ${response.status}`)
                  //   }

                  //   const reader = response.body.getReader();
                  //   const decoder = new TextDecoder('utf-8');
                  //   const encoder = new TextEncoder();

                  //   const readableStream = new ReadableStream({
                  //     async start(controller) {
                  //       function push() {
                  //         reader
                  //           .read()
                  //           .then(({ done, value }) => {
                  //             if (done) {
                  //               controller.close();
                  //               return;
                  //             }
                  //             const chunk = decoder.decode(value, { stream: true });
                  //             const message = chunk.replace('data: ', '');
                  //             controller.enqueue(encoder.encode(message))

                  //             // const parsed = JSON.parse(message);
                  //             // controller.enqueue(encoder.encode(parsed.choices[0].delta.content));
                  //             push();
                  //           })
                  //           .catch((err) => {
                  //             console.error('读取流中的数据时发生错误', err);
                  //             controller.error(err);
                  //           });
                  //       }
                  //       push();
                  //     },
                  //   });
                  //   return new Response(readableStream);
                  // }}
                  request={async (messages: any) => {

                    // 正常业务中如下:
                    const response = await fetch('/stream-sse', {
                      method: 'POST',
                      headers: {
                        'Content-Type': 'application/json;charset=UTF-8',
                      },
                      body: JSON.stringify({
                        messages,
                        stream: true,
                      }),
                    });
                    console.log('messages', messages);

                    // const mockResponse = new MockSSEResponse(dataArray);
                    // const response = mockResponse.getResponse();

                    // 确保服务器响应是成功的
                    if (!response.ok || !response.body) {
                      throw new Error(`HTTP error! status: ${response.status}`);
                    }

                    console.log('getting response');
                    const decoder = new TextDecoder('utf-8');
                    const encoder = new TextEncoder();
                    const reader = response.body?.getReader()

                    const readableStream = new ReadableStream({
                      async start(controller) {
                        function push() {
                          reader.read().then(({ done, value }) => {
                            // If there is no more data to read
                            if (done) {
                              console.log("done", done);
                              controller.close();
                              return;
                            }

                            console.log(done, value);

                            const chunk = decoder.decode(value, { stream: true })

                            // Check chunks by logging to the console
                            console.log(done, chunk);

                            // Get the data and send it to the browser via the controller
                            controller.enqueue(encoder.encode(chunk));


                            push();
                          });
                        }

                        push();
                      },
                    })


                    return new Response(readableStream);

                  }}
                />
              </div> 
            </div>
          </Content>
          <Footer style={{ textAlign: 'center' }}>
            NTU <a href='https://trustful.federated-learning.org/' target='blank'>Trustworthy Federated Ubiquitous Learning (TrustFUL) Research Lab</a>
          </Footer>
        </Layout>
      </Layout>



    </div>
  );
}

export default App;
