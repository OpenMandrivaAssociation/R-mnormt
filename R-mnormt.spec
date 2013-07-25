%global packname  mnormt
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4
Release:          5
Summary:          The multivariate normal and t distributions
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/mnormt/index.html
Source0:          http://cran.r-project.org/src/contrib/mnormt_1.4-5.tar.gz
BuildRequires:    R-devel

%description
This package provides functions for computing the density and the distribution
function of multivariate normal and multivariate "t" variates, and for 
generating random vectors sampled from these distributions. Probabilities are
computed via a non-Monte Carlo method; different routines are used 
for the case d=1, d=2, d>2, if d denotes the number of dimensions.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R