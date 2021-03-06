#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-asciidoctor
Version  : 1.5.4
Release  : 8
URL      : https://rubygems.org/downloads/asciidoctor-1.5.4.gem
Source0  : https://rubygems.org/downloads/asciidoctor-1.5.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-asciidoctor-bin
BuildRequires : ruby
BuildRequires : rubygem-coderay
BuildRequires : rubygem-cucumber
BuildRequires : rubygem-erubis
BuildRequires : rubygem-haml
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-minitest
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-slim
BuildRequires : rubygem-tilt

%description
= Asciidoctor
Dan Allen <https://github.com/mojavelinux[@mojavelinux]>; Sarah White <https://github.com/graphitefriction[@graphitefriction]>; Ryan Waldron <https://github.com/erebor[@erebor]>
v1.5.4, 2016-01-05
// settings:
:page-layout: base
:idprefix:
:idseparator: -
:source-language: ruby
:language: {source-language}
ifdef::env-github[:badges:]
// URIs:
:uri-org: https://github.com/asciidoctor
:uri-repo: {uri-org}/asciidoctor
:uri-asciidoctorj: {uri-org}/asciidoctorj
:uri-asciidoctorjs: {uri-org}/asciidoctor.js
:uri-project: http://asciidoctor.org
ifdef::awestruct-version[:uri-project: link:]
:uri-docs: {uri-project}/docs
:uri-news: {uri-project}/news
:uri-manpage: {uri-project}/man/asciidoctor
:uri-issues: {uri-repo}/issues
:uri-contributors: {uri-repo}/graphs/contributors
:uri-rel-file-base: link:
:uri-rel-tree-base: link:
ifdef::awestruct-version[]
:uri-rel-file-base: {uri-repo}/blob/master/
:uri-rel-tree-base: {uri-repo}/tree/master/
endif::[]
:uri-changelog: {uri-rel-file-base}CHANGELOG.adoc
:uri-contribute: {uri-rel-file-base}CONTRIBUTING.adoc
:uri-license: {uri-rel-file-base}LICENSE.adoc
:uri-tests: {uri-rel-tree-base}test
:uri-discuss: http://discuss.asciidoctor.org
:uri-irc: irc://irc.freenode.org/#asciidoctor
:uri-rubygem: https://rubygems.org/gems/asciidoctor
:uri-what-is-asciidoc: {uri-docs}/what-is-asciidoc
:uri-user-manual: {uri-docs}/user-manual
:uri-install-docker: https://github.com/asciidoctor/docker-asciidoctor
//:uri-install-doc: {uri-docs}/install-toolchain
:uri-install-osx-doc: {uri-docs}/install-asciidoctor-macosx
:uri-render-doc: {uri-docs}/render-documents
:uri-themes-doc: {uri-docs}/produce-custom-themes-using-asciidoctor-stylesheet-factory
:uri-gitscm-repo: https://github.com/git/git-scm.com
:uri-prototype: {uri-gitscm-repo}/commits/master/lib/asciidoc.rb
:uri-freesoftware: https://www.gnu.org/philosophy/free-sw.html
:uri-foundation: http://foundation.zurb.com
:uri-tilt: https://github.com/rtomayko/tilt
:uri-ruby: https://ruby-lang.org
// images:
:image-uri-screenshot: https://raw.githubusercontent.com/asciidoctor/asciidoctor/master/screenshot.png

%package bin
Summary: bin components for the rubygem-asciidoctor package.
Group: Binaries

%description bin
bin components for the rubygem-asciidoctor package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n asciidoctor-1.5.4
gem spec %{SOURCE0} -l --ruby > rubygem-asciidoctor.gemspec

%build
export LANG=C
gem build rubygem-asciidoctor.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
asciidoctor-1.5.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/asciidoctor-1.5.4
ruby -v -I.:lib:test test*/test_*.rb
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/asciidoctor-1.5.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/CHANGELOG.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/CONTRIBUTING.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/LICENSE.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/README.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/bin/asciidoctor
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/bin/asciidoctor-safe
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/data/stylesheets/asciidoctor-default.css
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/data/stylesheets/coderay-asciidoctor.css
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/features/open_block.feature
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/features/pass_block.feature
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/features/step_definitions.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/features/text_formatting.feature
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/features/xref.feature
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/abstract_block.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/abstract_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/attribute_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/block.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/callouts.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/cli/invoker.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/cli/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/composite.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/docbook45.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/docbook5.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/factory.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/html5.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/manpage.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/converter/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/core_ext/object/nil_or_empty.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/core_ext/string/chr.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/core_ext/symbol/length.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/inline.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/list.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/path_resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/reader.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/section.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/stylesheets.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/substitutors.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/table.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/timings.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/lib/asciidoctor/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/man/asciidoctor.1
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/man/asciidoctor.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/attributes_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/blocks_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/converter_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/document_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/extensions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/asciidoc_index.txt
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/basic-docinfo-footer.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/basic-docinfo-footer.xml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/basic-docinfo.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/basic-docinfo.xml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/basic.asciidoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/chapter-a.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/child-include.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/circle.svg
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/erb/html5/block_paragraph.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/haml/docbook45/block_paragraph.xml.haml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/haml/html5-tweaks/block_paragraph.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/haml/html5/block_paragraph.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/haml/html5/block_sidebar.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/slim/docbook45/block_paragraph.xml.slim
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/slim/html5/block_paragraph.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-backends/slim/html5/block_sidebar.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-docinfodir/basic-docinfo.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/custom-docinfodir/docinfo.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/docinfo-footer.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/docinfo-footer.xml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/docinfo.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/docinfo.xml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/dot.gif
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/encoding.asciidoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/grandchild-include.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/hello-asciidoctor.pdf
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/include-file.asciidoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/include-file.xml
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/master.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/parent-include-restricted.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/parent-include.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/sample.asciidoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/stylesheets/custom.css
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/subs-docinfo.html
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/subs.adoc
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/fixtures/tip.gif
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/invoker_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/links_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/lists_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/manpage_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/paragraphs_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/parser_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/paths_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/preamble_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/reader_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/sections_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/substitutions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/tables_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/asciidoctor-1.5.4/test/text_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/asciidoctor-1.5.4.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/asciidoctor
/usr/bin/asciidoctor-safe
