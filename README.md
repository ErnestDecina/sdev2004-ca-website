# SDEV2004 Continuous Assessment Website

A travel website that will serve information about Korean and Sweeden.

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
- [ ] Create Translations
- [ ] Documentation
- [ ] Presentation
- [ ] Optional: Host Website
  - [ ] Get Domain
  - [ ] Setup VPS

## Translation of Website

### Create new translation for Korea

``` bash
pybabel init -i ./translations/messages.pot -d translations -l ko
```

### Create new translation for Sweden

``` bash
pybabel init -i ./translations/messages.pot -d translations -l sv
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
