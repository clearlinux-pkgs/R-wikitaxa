#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-wikitaxa
Version  : 0.4.0
Release  : 35
URL      : https://cran.r-project.org/src/contrib/wikitaxa_0.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/wikitaxa_0.4.0.tar.gz
Summary  : Taxonomic Information from 'Wikipedia'
Group    : Development/Tools
License  : MIT
Requires: R-WikidataR
Requires: R-crul
Requires: R-curl
Requires: R-data.table
Requires: R-jsonlite
Requires: R-tibble
Requires: R-xml2
BuildRequires : R-WikidataR
BuildRequires : R-crul
BuildRequires : R-curl
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
'Wikispecies', and 'Wikidata'. Functions included for getting
    taxonomic information from each of the sources just listed, as
    well performing taxonomic search.

%prep
%setup -q -c -n wikitaxa
cd %{_builddir}/wikitaxa

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641149068

%install
export SOURCE_DATE_EPOCH=1641149068
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wikitaxa
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wikitaxa
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wikitaxa
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc wikitaxa || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/wikitaxa/DESCRIPTION
/usr/lib64/R/library/wikitaxa/INDEX
/usr/lib64/R/library/wikitaxa/LICENSE
/usr/lib64/R/library/wikitaxa/Meta/Rd.rds
/usr/lib64/R/library/wikitaxa/Meta/data.rds
/usr/lib64/R/library/wikitaxa/Meta/features.rds
/usr/lib64/R/library/wikitaxa/Meta/hsearch.rds
/usr/lib64/R/library/wikitaxa/Meta/links.rds
/usr/lib64/R/library/wikitaxa/Meta/nsInfo.rds
/usr/lib64/R/library/wikitaxa/Meta/package.rds
/usr/lib64/R/library/wikitaxa/Meta/vignette.rds
/usr/lib64/R/library/wikitaxa/NAMESPACE
/usr/lib64/R/library/wikitaxa/NEWS.md
/usr/lib64/R/library/wikitaxa/R/wikitaxa
/usr/lib64/R/library/wikitaxa/R/wikitaxa.rdb
/usr/lib64/R/library/wikitaxa/R/wikitaxa.rdx
/usr/lib64/R/library/wikitaxa/data/Rdata.rdb
/usr/lib64/R/library/wikitaxa/data/Rdata.rds
/usr/lib64/R/library/wikitaxa/data/Rdata.rdx
/usr/lib64/R/library/wikitaxa/doc/index.html
/usr/lib64/R/library/wikitaxa/doc/wikitaxa.Rmd
/usr/lib64/R/library/wikitaxa/doc/wikitaxa.html
/usr/lib64/R/library/wikitaxa/help/AnIndex
/usr/lib64/R/library/wikitaxa/help/aliases.rds
/usr/lib64/R/library/wikitaxa/help/paths.rds
/usr/lib64/R/library/wikitaxa/help/wikitaxa.rdb
/usr/lib64/R/library/wikitaxa/help/wikitaxa.rdx
/usr/lib64/R/library/wikitaxa/html/00Index.html
/usr/lib64/R/library/wikitaxa/html/R.css
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_data.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wiki_page.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wiki_page_non_empty.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wiki_page_non_empty_common_names.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikicommons1.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikicommons2.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikicommons_parse.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikicommons_search.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikicommons_search_not_found.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikipedia_malus.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikipedia_parse.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikipedia_poa.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikipedia_search.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikipedia_search_not_found.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikispecies_malus.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikispecies_parse.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikispecies_poa.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikispecies_search.yml
/usr/lib64/R/library/wikitaxa/tests/fixtures/vcr_cassettes/wt_wikispecies_search_not_found.yml
/usr/lib64/R/library/wikitaxa/tests/test-all.R
/usr/lib64/R/library/wikitaxa/tests/testthat/helper-wikitaxa.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wikicommons.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wikipedia.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wikispecies.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wt_data.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wt_wiki_page.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wt_wiki_url_build.R
/usr/lib64/R/library/wikitaxa/tests/testthat/test-wt_wiki_url_parse.R
