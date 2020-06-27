Name:           python-matrix-nio
Version:        0.6
Release:        0
License:        ISC
Summary:        A Python Matrix client library, designed according to sans I/O principles
Url:            https://github.com/poljar/matrix-nio
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/matrix-nio/matrix-nio-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module h11}
BuildRequires:  %{python_module h2}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module logbook}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module unpaddedbase64}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs
Requires:       python-future
Requires:       python-h11
Requires:       python-h2
Requires:       python-jsonschema
Requires:       python-logbook
Requires:       python-pycryptodome
Requires:       python-unpaddedbase64
Suggests:       python-typing
Suggests:       python-aiohttp
Suggests:       python-python-olm >= 3.1.0
Suggests:       python-peewee >= 3.9.5
Suggests:       python-cachetools
Suggests:       python-atomicwrites
BuildArch:      noarch

%python_subpackages

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep
%setup -q -n matrix-nio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*
