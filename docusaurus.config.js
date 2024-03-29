// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

const organizationName = "NubeIO";
const projectName = "rubix-ce-docs";
const deploymentBranch = "deployment"



/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Document',
  tagline: '',
  favicon: 'https://nube-io.com/wp-content/uploads/2021/06/cropped-index-32x32.png',

  // Set the production url of your site here
   url: `https://${organizationName}.github.io`,
   baseUrl: `/${projectName}/`,
  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName, // Usually your GitHub org/user name.
  projectName, // Usually your repo name.
  deploymentBranch,

  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
         // editUrl: `https://github.com/${organizationName}/${projectName}/tree/main/`,
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: `https://github.com/${organizationName}/${projectName}/tree/main/`,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'https://nube-io.com/wp-content/uploads/2022/04/Nube-logo.png',
      navbar: {
        title: 'Home',
        logo: {
          alt: 'My Site Logo',
          src: 'https://nube-io.com/wp-content/uploads/2022/04/Nube-logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {
            type: 'docsVersionDropdown',
            position: 'right',
            dropdownItemsAfter: [{to: '/versions', label: 'All versions'}],
            dropdownActiveClassDisabled: true,
          },
        ],
      },
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      footer: {
        // style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Rubix-CE',
                to: '/docs/overview',
              },
            ],
          },
          {
            title: 'Nube IO',
            items: [
              {
                label: 'Nube-IO Home Page',
                href: 'https://nube-io.com/',
              },
              {
                label: 'Old Nube-IO Documents Site',
                href: 'https://nubeio.zohodesk.com.au/portal/en/kb/nube-io',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'info on BACnet',
                href: 'https://en.wikipedia.org/wiki/BACnet',
              },
              {
                label: 'info on Modbus',
                href: 'https://en.wikipedia.org/wiki/Modbus',
              },
            ],
          },
        ],
        copyright: `Copyright© Nube-iO ${new Date().getFullYear()}`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),

  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

};

module.exports = config;
