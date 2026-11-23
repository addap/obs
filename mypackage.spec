#
# spec file for package mypackage
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           mypackage
Version:        1.0
Release:        0
License:        MIT
Summary:        Dummy package
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Dummy text

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
touch %{buildroot}%{_datadir}/%{name}/CONTENT

%files
%defattr(-,root,root)
%{_datadir}/%{name}/CONTENT

%changelog
