SCHEMA = {
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "typeName" : "AWS::EC2::SecurityGroupEgress",
  "readOnlyProperties" : [ "/properties/Id" ],
  "description" : "Adds the specified outbound (egress) rule to a security group.\n An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).\n You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.\n You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.\n Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.",
  "createOnlyProperties" : [ "/properties/IpProtocol", "/properties/DestinationSecurityGroupId", "/properties/ToPort", "/properties/CidrIp", "/properties/FromPort", "/properties/GroupId", "/properties/CidrIpv6", "/properties/DestinationPrefixListId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "required" : [ "IpProtocol", "GroupId" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "propertyTransform" : {
    "/properties/IpProtocol" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$mapVal ? $mapVal : $lowercase(IpProtocol))",
    "/properties/ToPort" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$ipProtocol := $mapVal ? $mapVal : $lowercase(IpProtocol);$ipProtocol in ['imcp', 'tcp', 'udp', 'imcp'] ? ToPort : -1)",
    "/properties/FromPort" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$ipProtocol := $mapVal ? $mapVal : $lowercase(IpProtocol);$ipProtocol in ['imcp', 'tcp', 'udp', 'imcp'] ? FromPort : -1)"
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "ec2:DescribeSecurityGroupRules" ]
    },
    "create" : {
      "permissions" : [ "ec2:AuthorizeSecurityGroupEgress", "ec2:RevokeSecurityGroupEgress", "ec2:DescribeSecurityGroupRules" ]
    },
    "update" : {
      "permissions" : [ "ec2:UpdateSecurityGroupRuleDescriptionsEgress" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeSecurityGroupRules" ]
    },
    "delete" : {
      "permissions" : [ "ec2:RevokeSecurityGroupEgress", "ec2:DescribeSecurityGroupRules" ]
    }
  },
  "additionalProperties" : False,
  "properties" : {
    "CidrIp" : {
      "description" : "The IPv4 address range, in CIDR format.\n You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.\n For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.",
      "type" : "string"
    },
    "CidrIpv6" : {
      "description" : "The IPv6 address range, in CIDR format.\n You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.\n For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of an egress (outbound) security group rule.\n Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "type" : "string"
    },
    "FromPort" : {
      "description" : "If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).",
      "type" : "integer"
    },
    "ToPort" : {
      "description" : "If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).",
      "type" : "integer"
    },
    "IpProtocol" : {
      "description" : "The IP protocol name (``tcp``, ``udp``, ``icmp``, ``icmpv6``) or number (see [Protocol Numbers](https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).\n Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp``, ``udp``, ``icmp``, or ``icmpv6`` allows traffic on all ports, regardless of any port range you specify. For ``tcp``, ``udp``, and ``icmp``, you must specify a port range. For ``icmpv6``, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.",
      "type" : "string"
    },
    "DestinationSecurityGroupId" : {
      "description" : "The ID of the security group.\n You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.",
      "type" : "string"
    },
    "Id" : {
      "description" : "",
      "type" : "string"
    },
    "DestinationPrefixListId" : {
      "description" : "The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.\n You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.",
      "type" : "string"
    },
    "GroupId" : {
      "description" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.",
      "type" : "string"
    }
  }
}