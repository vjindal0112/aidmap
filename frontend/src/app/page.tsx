"use client";

import Image from "next/image";
import {Inter} from "@next/font/google";
import styles from "./page.module.css";
import React from "react";
import {
  Navbar,
  Button,
  Link,
  Radio,
  Container,
  Grid,
  Card,
  Text,
  Spacer,
  createTheme,
  NextUIProvider,
} from "@nextui-org/react";
import FeedBeeLogo from "@/components/FeedBeeLogo";

const inter = Inter({subsets: ["latin"]});

const theme = createTheme({
  type: "light", // it could be "light" or "dark"
  theme: {
    colors: {
      primary: "$red600",
      secondary: "$yellow600",
      secondaryLight: "$yellow400",
      secondaryLightContrast: "$red800",
      secondaryLightHover: "$yellow500",
    },
    space: {},
    fonts: {},
  },
});

export default function Home() {
  return (
    <NextUIProvider theme={theme}>
      <style jsx global>{`
        * {
          font-family: ${inter.style.fontFamily};
        }
      `}</style>
      <Navbar isBordered variant="sticky">
        <Navbar.Brand>
          <FeedBeeLogo />
        </Navbar.Brand>
        <Navbar.Content activeColor="primary" hideIn="xs">
          <Navbar.Item>
            <Button auto light as={Link} href="#">
              Login
            </Button>
          </Navbar.Item>
          <Navbar.Item>
            <Button auto flat as={Link} color="secondary" href="#">
              Sign Up
            </Button>
          </Navbar.Item>
        </Navbar.Content>
      </Navbar>
      <main className={`${styles.main} ${inter.className}`}>
        <Spacer y={6} />
        <Grid.Container
          direction="column"
          alignItems="center"
          justify="center"
          css={{textAlign: "center"}}
        >
          <Text
            h1
            size={60}
            css={{
              textGradient: "45deg, $yellow600 30%, $red500 90%",
              marginRight: "2em",
              marginLeft: "2em",
            }}
            weight="extrabold"
          >
            FeedBee simplifies feedback for your newsletter
          </Text>
          <Text size={18}>
            Get actionable feedback from your readers seamlessly with 1-click
            surveys
          </Text>
          <Spacer y={2} />
          <Button rounded>
            <b>&nbsp;Get started &nbsp;</b>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="white">
              <path d="M5.46967 11.4697C5.17678 11.7626 5.17678 12.2374 5.46967 12.5303C5.76256 12.8232 6.23744 12.8232 6.53033 12.5303L10.5303 8.53033C10.8207 8.23999 10.8236 7.77014 10.5368 7.47624L6.63419 3.47624C6.34492 3.17976 5.87009 3.17391 5.57361 3.46318C5.27713 3.75244 5.27128 4.22728 5.56054 4.52376L8.94583 7.99351L5.46967 11.4697Z"></path>
            </svg>
          </Button>
        </Grid.Container>

        <Spacer y={6} />
      </main>
      <main>
        <Grid.Container
          justify="center"
          alignItems="center"
          css={{padding: "12px"}}
          gap={5}
        >
          <Grid xs={1}></Grid>
          <Grid
            xs
            direction="column"
            alignItems="center"
            css={{textAlign: "center"}}
          >
            <Text h3>Get actionable feedback</Text>
            <Spacer y={0.25} />
            <Text>Readers can give you feedback with a single click.</Text>
          </Grid>
          <Grid xs={6} alignItems="center" direction="column">
            <Image
              height={325}
              width={600}
              alt="FeedBee from the reader's perspective GIF"
              src="https://raw.githubusercontent.com/Feed-Bee/feedbee-images/main/feedbee-reader-perspective.webp"
            />
          </Grid>

          <Grid xs={1}></Grid>
        </Grid.Container>
      </main>
      <main>
        <Grid.Container
          justify="center"
          alignItems="center"
          css={{padding: "12px"}}
          gap={5}
        >
          <Grid xs={1}></Grid>
          <Grid xs={6} alignItems="center" direction="column">
            <Image
              height={325}
              width={600}
              alt="FeedBee from the writers's perspective GIF"
              src="https://raw.githubusercontent.com/Feed-Bee/feedbee-images/main/feedbee-writer-perspective-email.webp"
            />
          </Grid>
          <Grid
            xs
            direction="column"
            alignItems="center"
            css={{textAlign: "center"}}
          >
            <Text h3>Quality Analytics</Text>
            <Spacer y={0.25} />
            <Text>Easy to understand graphs in your inbox every week.</Text>
          </Grid>

          <Grid xs={1}></Grid>
        </Grid.Container>
      </main>
      <Spacer y={6} />
      <main>
        <Grid.Container
          justify="center"
          alignItems="center"
          css={{padding: "12px", textAlign: "center"}}
          gap={2}
        >
          <Grid>
            <Text
              h1
              size={60}
              css={{
                textGradient: "45deg, $yellow600 30%, $red500 90%",
                marginRight: "2em",
                marginLeft: "2em",
              }}
              weight="extrabold"
            >
              Built to help you grow your newsletter
            </Text>
          </Grid>
          <Grid
            direction="column"
            alignItems="center"
            css={{textAlign: "center"}}
          >
            <Button rounded>
              <b>Get set up</b>
            </Button>
          </Grid>
        </Grid.Container>
      </main>

      <Spacer y={8} />
    </NextUIProvider>
  );
}
