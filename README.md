# SDEV2004 Continuous Assessment Website

## Updated Documentation

[Word Documentation](https://1drv.ms/w/s!Ats780sGNINomRlL078S1AlXuPbA?e=IwNpiD)

## Roadmap

- [x] Setup
- [x] Persona's
- [x] Wireframes
- [x] Create Webpages  
  - [x] Header
  - [x] Footer
  - [x] Content
- [x] Create Translations
- [x] Documentation
- [ ] Presentation
- [x] Optional: Host Website
  - [x] Get Domain
  - [x] Setup VPS

## Translation of Website
Make sure to be in the sdev2004-ca-website/app directory

### Extract Text
``` bash
pybabel extract -F configs/babel.cfg -k _l -o translations/messages.pot .
```

### Create new translation for Korea

``` bash
pybabel init -i ./translations/messages.pot -d translations -l ko
```

### Create new translation for Sweden

``` bash
pybabel init -i ./translations/messages.pot -d translations -l sv
```

### Updating translations for Korea
``` bash
pybabel update -i .\translations\messages.pot -d .\translations\
```

### Updating translations for Sweden
``` bash
pybabel update -i .\translations\messages.pot -d .\translations\
```

### Compiling translations

``` bash
pybabel compile -d translations
```

## Authors

- Daniel Wu - [Daniel Wu](https://github.com/Dan21460)
- Ernest John Decina - [ErnestDecina](https://github.com/ErnestDecina)
- Michael O'Brien - [Michael O'Brien](https://github.com/mobrien273)
- Ron Pingol - [ronpingol](https://github.com/ronpingol)
- Sean Tighe - [KindPlayer2](https://github.com/KindPlayer2)
- Alex Tsang - [Entroshock](https://github.com/Entroshock)
  
## [License](LICENSE.md)

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
