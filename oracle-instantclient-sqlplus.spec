Name:           gqlplus
Version:        1.15
Release:        0
License:        GPL-2.0
Summary:        A drop-in replacement for sqlplus, an Oracle SQL client
Url:            http://gqlplus.sourceforge.net/
Group:          Productivity/Databases/Clients
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc make autoconf automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       oracle-instantclient-sqlplus
%description
GQLPlus is a drop-in replacement for sqlplus, an Oracle SQL client, for UNIX and UNIX-like platforms. The difference between GQLPlus and sqlplus is command-line editing and history, plus table-name and column-name completion.

%prep
%setup -q

%build
aclocal && autoconf
automake --add-missing
%configure
make %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-,root,root)
%doc ChangeLog README LICENSE
%{_bindir}/gqlplus

%changelog
