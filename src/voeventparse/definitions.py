"""This module simply serves to store the XML schema, a 'skeleton' VOEvent
xml document for creation of new instances, and various other minor definitions.

These values may be used in place of literal strings, to allow autocompletion
and document the fact that they are 'standardized' values.
"""
from __future__ import unicode_literals
from six import b

# ############################
# Some useful string defs namespaced via a class container:

class roles:
    observation = 'observation'
    prediction = 'prediction'
    utility = 'utility'
    test = 'test'


class sky_coord_system:
    """
    Common coordinate system identifiers. See also :class:`.Position2D`.

    This is not a simple combinatorial mix of all components, it's a
    reproduction of the enumeration in the XML schema. Note some entries in the
    schema enumeration are repeated, which leads me to think it may be flawed,
    but that's an investigation for another day.

    """
    gps_fk5_topo = 'GPS-FK5-TOPO'
    gps_icrs_geo = 'GPS-ICRS-GEO'
    gps_icrs_topo = 'GPS-ICRS-TOPO'

    tdb_fk5_bary = 'TDB-FK5-BARY'
    tdb_icrs_bary = 'TDB-ICRS-BARY'

    tt_fk5_geo = 'TT-FK5-GEO'
    tt_fk5_topo = 'TT-FK5-TOPO'
    tt_icrs_geo = 'TT-ICRS-GEO'
    tt_icrs_topo = 'TT-ICRS-TOPO'

    utc_fk5_geo = 'UTC-FK5-GEO'
    utc_fk5_topo = 'UTC-FK5-TOPO'
    utc_icrs_geo = 'UTC-ICRS-GEO'
    utc_icrs_topo = 'UTC-ICRS-TOPO'




class observatory_location(object):
    """Common generic values for the WhereWhen.ObservatoryLocation attribute."""
    geosurface = 'GEOSURFACE'
    geolunar = 'GEOLUN'


class units:
    """
    Unit abbreviations as defined by CDS (incomplete listing)

    cf http://vizier.u-strasbg.fr/doc/catstd-3.2.htx
    """
    degree = 'deg'
    degrees = degree #Alias for backwards compatibility. Singular otherwise.
    arcsecond = 'arcsec'
    milliarcsecond = 'mas'

    day = 'd'
    hour = 'h'
    minute = 'min'
    year = 'yr'

    count = 'ct'
    hertz = 'Hz'
    jansky = 'Jy'
    magnitude = 'mag'



class cite_types:
    """Possible types of :func:`.EventIvorn`"""
    followup = 'followup'
    supersedes = 'supersedes'
    retraction = 'retraction'

####################################
#: Skeleton XML for instantiating a new VOEvent tree
v2_0_skeleton_str = b"""<?xml version="1.0" ?>
<voe:VOEvent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:voe="http://www.ivoa.net/xml/VOEvent/v2.0"
    xsi:schemaLocation="http://www.ivoa.net/xml/VOEvent/v2.0 http://www.ivoa.net/xml/VOEvent/VOEvent-v2.0.xsd"
    version="2.0"
    role="test"
    ivorn="ivo://undefined">
</voe:VOEvent>
"""

####################################
#: VOEvent 2.0 schema for validation
#Schema downloaded from:
#http://www.ivoa.net/xml/VOEvent/VOEvent-v2.0.xsd
v2_0_schema_str = b"""<?xml version="1.0"?>
<xs:schema xmlns="http://www.ivoa.net/xml/VOEvent/v2.0" xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="http://www.ivoa.net/xml/VOEvent/v2.0" elementFormDefault="unqualified">

  <xs:element name="VOEvent">
    <xs:annotation>
      <xs:documentation> VOEvent is the root element for describing observations of immediate
        astronomical events. For more information, see
        http://www.ivoa.net/twiki/bin/view/IVOA/IvoaVOEvent. The event consists of at most one of
        each of: Who, What, WhereWhen, How, Why, Citations, Description, and
        Reference.</xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <!-- Can have zero or one of each of these, in any order -->
      <xs:all>
        <xs:element name="Who"         type="Who"       minOccurs="0" maxOccurs="1"/>
        <xs:element name="What"        type="What"      minOccurs="0" maxOccurs="1"/>
        <xs:element name="WhereWhen"   type="WhereWhen" minOccurs="0" maxOccurs="1"/>
        <xs:element name="How"         type="How"       minOccurs="0" maxOccurs="1"/>
        <xs:element name="Why"         type="Why"       minOccurs="0" maxOccurs="1"/>
        <xs:element name="Citations"   type="Citations" minOccurs="0" maxOccurs="1"/>
        <xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1"/>
        <xs:element name="Reference"   type="Reference" minOccurs="0" maxOccurs="1"/>
      </xs:all>
      <xs:attribute name="version"     type="xs:token"   fixed="2.0" use="required"/>
      <xs:attribute name="ivorn"       type="xs:anyURI"  use="required"/>
      <xs:attribute name="role"        type="roleValues" default="observation"/>
    </xs:complexType>
  </xs:element>
  <xs:simpleType name="roleValues">
    <xs:restriction base="xs:string">
      <xs:enumeration value="observation"/>
      <xs:enumeration value="prediction"/>
      <xs:enumeration value="utility"/>
      <xs:enumeration value="test"/>
    </xs:restriction>
  </xs:simpleType>


  <xs:complexType name="Who">
    <xs:annotation>
      <xs:documentation> Who: Curation Metadata </xs:documentation>
    </xs:annotation>
    <xs:all>
      <!-- Can have zero or one of each of these. Schema is loose because
        should have AuthorIVORN *or* Author -->
      <xs:element name="AuthorIVORN" type="xs:anyURI" minOccurs="0"/>
      <xs:element name="Date" type="xs:dateTime" minOccurs="0"/>
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0"/>
      <xs:element name="Author" minOccurs="0">
        <xs:annotation>
          <xs:documentation> Author information follows the IVOA curation information schema: the
            organization responsible for the packet can have a title, short name or acronym, and a
            logo. A contact person has a name, email, and phone number. Other contributors can also
            be noted. </xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:choice maxOccurs="unbounded">
            <xs:element name="title" type="xs:string"/>
            <xs:element name="shortName" type="xs:string"/>
            <xs:element name="logoURL" type="xs:anyURI"/>
            <xs:element name="contactName" type="xs:string"/>
            <xs:element name="contactEmail" type="xs:string"/>
            <xs:element name="contactPhone" type="xs:string"/>
            <xs:element name="contributor" type="xs:string"/>
          </xs:choice>
        </xs:complexType>
      </xs:element>
    </xs:all>
  </xs:complexType>


  <xs:complexType name="What">
    <xs:annotation>
      <xs:documentation> What: Event Characterization. This is the part of the data model that is
        chosen by the Authoer of the event rather than the IVOA. There can be Params, that may be in
        Groups, and Tables, and simpleTimeSeries. There can also be Description and Reference as
        with most VOEvent elements. </xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <!-- can have any number of any of these in any order  -->
      <xs:element name="Param" type="Param" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Group" type="Group" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Table" type="Table" minOccurs="0" maxOccurs="unbounded"/>
      <!--<xs:element ref="sts:SimpleTimeseries"          minOccurs="0" maxOccurs="unbounded"/>-->
      <xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Reference" type="Reference" minOccurs="0" maxOccurs="unbounded"/>
    </xs:choice>
  </xs:complexType>


  <xs:complexType name="Param">
    <xs:annotation>
      <xs:documentation> What/Param definition. A Param has name, value, ucd, unit, dataType; and
        may have Description and Reference.</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Value" type="xs:string" minOccurs="0" maxOccurs="1"/>
    </xs:choice>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="ucd" type="xs:string"/>
    <xs:attribute name="value" type="xs:string"/>
    <xs:attribute name="unit" type="xs:string"/>
    <xs:attribute name="dataType" type="dataType" default="string"/>
    <xs:attribute name="utype" type="xs:string"/>
  </xs:complexType>
  <xs:simpleType name="dataType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="string"/>
      <xs:enumeration value="float"/>
      <xs:enumeration value="int"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="Group">
    <xs:annotation>
      <xs:documentation> What/Group definition: A group is a collection of Params, with name and
        type attributes.</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Param" type="Param" maxOccurs="unbounded"/>
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0"/>
    </xs:choice>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="type" type="xs:string"/>
  </xs:complexType>


  <xs:complexType name="Table">
    <xs:annotation>
      <xs:documentation> What/Table definition. This small Table has Fields for the column
        definitions, and Data to hold the table data, with TR for row and TD for value of a table
        cell.</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0"/>
      <xs:element name="Param" type="Param" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Field" type="Field" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Data" type="Data" minOccurs="1" maxOccurs="1"/>
    </xs:choice>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="type" type="xs:string"/>
  </xs:complexType>
  <xs:complexType name="Field">
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0"/>
    </xs:choice>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="ucd" type="xs:string"/>
    <xs:attribute name="unit" type="xs:string"/>
    <xs:attribute name="dataType" type="dataType" default="string"/>
    <xs:attribute name="utype" type="xs:string"/>
  </xs:complexType>
  <xs:complexType name="Data">
    <xs:choice maxOccurs="unbounded">
      <xs:element name="TR" type="TR"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="TR">
    <xs:choice maxOccurs="unbounded">
      <xs:element name="TD" type="xs:string"/>
    </xs:choice>
  </xs:complexType>


  <xs:complexType name="WhereWhen">
    <xs:annotation>
      <xs:documentation> WhereWhen: Space-Time Coordinates. Lots and lots of elements here, but the
        import is that each event has these: observatory, sky_coord_system, time, timeError, longitude,
        latitude, posError.</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="ObsDataLocation" type="ObsDataLocation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
      <xs:element name="Reference" type="Reference" minOccurs="0"/>
    </xs:choice>
    <xs:attribute name="id" type="xs:ID" use="optional"/>
  </xs:complexType>

  <xs:complexType name="ObsDataLocation">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="ObservatoryLocation" minOccurs="1" maxOccurs="1" type="ObservatoryLocation"/>
      <xs:element name="ObservationLocation" minOccurs="1" maxOccurs="1" type="ObservationLocation"/>
    </xs:all>
  </xs:complexType>

  <xs:complexType name="ObservationLocation">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="AstroCoordSystem" type="AstroCoordSystem" minOccurs="1" maxOccurs="1"/>
      <xs:element name="AstroCoords" type="AstroCoords" minOccurs="1" maxOccurs="1"/>
    </xs:all>
  </xs:complexType>

  <xs:complexType name="AstroCoordSystem">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <!-- The empty sequence closes this to content -->
    <xs:sequence />
    <xs:attribute name="id" type="idValues"/>
  </xs:complexType>
  <xs:simpleType name="idValues">
    <xs:restriction base="xs:string">
      <xs:enumeration value="TT-ICRS-TOPO"/>
      <xs:enumeration value="UTC-ICRS-TOPO"/>
      <xs:enumeration value="TT-FK5-TOPO"/>
      <xs:enumeration value="UTC-FK5-TOPO"/>
      <xs:enumeration value="GPS-ICRS-TOPO"/>
      <xs:enumeration value="GPS-ICRS-TOPO"/>
      <xs:enumeration value="GPS-FK5-TOPO"/>
      <xs:enumeration value="GPS-FK5-TOPO"/>
      <xs:enumeration value="TT-ICRS-GEO"/>
      <xs:enumeration value="UTC-ICRS-GEO"/>
      <xs:enumeration value="TT-FK5-GEO"/>
      <xs:enumeration value="UTC-FK5-GEO"/>
      <xs:enumeration value="GPS-ICRS-GEO"/>
      <xs:enumeration value="GPS-ICRS-GEO"/>
      <xs:enumeration value="TDB-ICRS-BARY"/>
      <xs:enumeration value="TDB-FK5-BARY"/>
      <!-- this one for ObservatoryLocation -->
      <xs:enumeration value="UTC-GEOD-TOPO"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="AstroCoords">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="Time" type="Time" minOccurs="0"/>
      <xs:element name="Position2D" type="Position2D" minOccurs="0"/>
      <xs:element name="Position3D" type="Position3D" minOccurs="0"/>
    </xs:all>
    <xs:attribute name="coord_system_id" type="idValues"/>
  </xs:complexType>

  <xs:complexType name="Time">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="TimeInstant" type="TimeInstant"/>
      <xs:element name="Error" type="xs:float" minOccurs="0"/>
    </xs:choice>
    <xs:attribute name="unit" type="xs:string"/>
  </xs:complexType>

  <xs:complexType name="TimeInstant">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="ISOTime" type="xs:string" minOccurs="0" maxOccurs="1"/>
      <xs:element name="TimeOffset" type="xs:float" minOccurs="0" maxOccurs="1"/>
      <xs:element name="TimeScale" type="xs:string" minOccurs="0" maxOccurs="1"/>
    </xs:choice>
  </xs:complexType>

  <xs:complexType name="Position2D">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="Name1" type="xs:string" minOccurs="0"/>
      <xs:element name="Name2" type="xs:string" minOccurs="0"/>
      <xs:element name="Value2" type="Value2"/>
      <xs:element name="Error2Radius" type="xs:float"/>
    </xs:all>
    <xs:attribute name="unit" type="xs:string"/>
  </xs:complexType>

  <xs:complexType name="Position3D">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="Name1" type="xs:string" minOccurs="0"/>
      <xs:element name="Name2" type="xs:string" minOccurs="0"/>
      <xs:element name="Name3" type="xs:string" minOccurs="0"/>
      <xs:element name="Value3" type="Value3"/>
    </xs:all>
    <xs:attribute name="unit" type="xs:string"/>
  </xs:complexType>

  <xs:complexType name="Value2">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="C1" type="xs:float"/>
      <xs:element name="C2" type="xs:float"/>
    </xs:all>
  </xs:complexType>

  <xs:complexType name="Value3">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="C1" type="xs:float"/>
      <xs:element name="C2" type="xs:float"/>
      <xs:element name="C3" type="xs:float"/>
    </xs:all>
  </xs:complexType>

  <xs:complexType name="ObservatoryLocation">
    <xs:annotation>
      <xs:documentation> Part of WhereWhen</xs:documentation>
    </xs:annotation>
    <xs:all>
      <xs:element name="AstroCoordSystem" type="AstroCoordSystem" minOccurs="0" maxOccurs="1"/>
      <xs:element name="AstroCoords" type="AstroCoords" minOccurs="0" maxOccurs="1"/>
    </xs:all>
    <xs:attribute name="id" type="xs:string"/>
  </xs:complexType>

  <xs:complexType name="How">
    <xs:annotation>
      <xs:documentation> How: Instrument Configuration. Built with some Description and Reference
        elements. </xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Description" type="xs:string"/>
      <xs:element name="Reference" type="Reference"/>
    </xs:choice>
  </xs:complexType>

  <xs:complexType name="Why">
    <xs:annotation>
      <xs:documentation> Why: Initial Scientific Assessment. Can make simple Concept/Name/Desc/Ref
        for the inference or use multiple Inference containers for more semantic sophistication.
      </xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Name" type="xs:string"/>
      <xs:element name="Concept" type="xs:string"/>
      <xs:element name="Inference" type="Inference"/>
      <xs:element name="Description" type="xs:string"/>
      <xs:element name="Reference" type="Reference"/>
    </xs:choice>
    <xs:attribute name="importance" type="xs:float"/>
    <xs:attribute name="expires" type="xs:dateTime"/>
  </xs:complexType>

  <xs:complexType name="Inference">
    <xs:annotation>
      <xs:documentation> Why/Inference: A container for a more nuanced expression, including
        relationships and probability. </xs:documentation>
    </xs:annotation>
    <xs:choice maxOccurs="unbounded">
      <xs:element name="Name" type="xs:string"/>
      <xs:element name="Concept" type="xs:string"/>
      <xs:element name="Description" type="xs:string"/>
      <xs:element name="Reference" type="Reference"/>
    </xs:choice>
    <xs:attribute name="probability" type="smallFloat"/>
    <xs:attribute name="relation" type="xs:string"/>
  </xs:complexType>
  <xs:simpleType name="smallFloat">
    <xs:restriction base="xs:float">
      <xs:minInclusive value="0.0"/>
      <xs:maxInclusive value="1.0"/>
    </xs:restriction>
  </xs:simpleType>


  <xs:complexType name="Citations">
    <xs:annotation>
      <xs:documentation> Citations: Follow-up Observations. This section is a sequence of EventIVORN
        elements, each of which has the IVORN of a cited event. </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="EventIVORN" type="EventIVORN" maxOccurs="unbounded"/>
      <xs:element name="Description" type="xs:string" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="EventIVORN">
    <xs:annotation>
      <xs:documentation> Citations/EventIVORN. The value is the IVORN of the cited event, the 'cite'
        attribute is the nature of that relationship, choosing from 'followup', 'supersedes', or
        'retraction'.</xs:documentation>
    </xs:annotation>
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="cite" type="citeValues"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:simpleType name="citeValues">
    <xs:restriction base="xs:string">
      <xs:enumeration value="followup"/>
      <xs:enumeration value="supersedes"/>
      <xs:enumeration value="retraction"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="Reference">
    <xs:annotation>
      <xs:documentation> Reference: External Content. The payload is the uri, and the 'type'
        describes the nature of the data under that uri. The Reference can also be named.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence/>
    <xs:attribute name="uri" type="xs:anyURI" use="required"/>
    <xs:attribute name="type" type="xs:string"/>
    <xs:attribute name="mimetype" type="xs:string"/>
    <xs:attribute name="meaning" type="xs:anyURI"/>
  </xs:complexType>

</xs:schema>
"""
