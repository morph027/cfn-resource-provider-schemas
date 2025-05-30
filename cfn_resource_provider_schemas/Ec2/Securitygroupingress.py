SCHEMA = {
  "typeName" : "AWS::EC2::SecurityGroupIngress",
  "description" : "Resource Type definition for AWS::EC2::SecurityGroupIngress",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "description" : "The Security Group Rule Id",
      "type" : "string"
    },
    "CidrIp" : {
      "description" : "The IPv4 ranges",
      "type" : "string"
    },
    "CidrIpv6" : {
      "description" : "[VPC only] The IPv6 ranges",
      "type" : "string"
    },
    "Description" : {
      "description" : "Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously",
      "type" : "string"
    },
    "FromPort" : {
      "description" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nUse this for ICMP and any protocol that uses ports.",
      "type" : "integer"
    },
    "GroupId" : {
      "description" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.\n\nYou must specify the GroupName property or the GroupId property. For security groups that are in a VPC, you must use the GroupId property.",
      "type" : "string"
    },
    "GroupName" : {
      "description" : "The name of the security group.",
      "type" : "string"
    },
    "IpProtocol" : {
      "description" : "The IP protocol name (tcp, udp, icmp, icmpv6) or number (see Protocol Numbers).\n\n[VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or icmpv6 allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For icmpv6, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.",
      "type" : "string"
    },
    "SourcePrefixListId" : {
      "description" : "[EC2-VPC only] The ID of a prefix list.\n\n",
      "type" : "string"
    },
    "SourceSecurityGroupId" : {
      "description" : "The ID of the security group. You must specify either the security group ID or the security group name. For security groups in a nondefault VPC, you must specify the security group ID.",
      "type" : "string"
    },
    "SourceSecurityGroupName" : {
      "description" : "[EC2-Classic, default VPC] The name of the source security group.\n\nYou must specify the GroupName property or the GroupId property. For security groups that are in a VPC, you must use the GroupId property.",
      "type" : "string"
    },
    "SourceSecurityGroupOwnerId" : {
      "description" : "[nondefault VPC] The AWS account ID that owns the source security group. You can't specify this property with an IP address range.\n\nIf you specify SourceSecurityGroupName or SourceSecurityGroupId and that security group is owned by a different account than the account creating the stack, you must specify the SourceSecurityGroupOwnerId; otherwise, this property is optional.",
      "type" : "string"
    },
    "ToPort" : {
      "description" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nUse this for ICMP and any protocol that uses ports.",
      "type" : "integer"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "IpProtocol" ],
  "createOnlyProperties" : [ "/properties/GroupName", "/properties/IpProtocol", "/properties/SourceSecurityGroupId", "/properties/SourcePrefixListId", "/properties/ToPort", "/properties/CidrIp", "/properties/SourceSecurityGroupName", "/properties/SourceSecurityGroupOwnerId", "/properties/FromPort", "/properties/GroupId", "/properties/CidrIpv6" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "propertyTransform" : {
    "/properties/IpProtocol" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$mapVal ? $mapVal : $lowercase(IpProtocol))",
    "/properties/FromPort" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$ipProtocol := $mapVal ? $mapVal : $lowercase(IpProtocol);$ipProtocol in ['imcp', 'tcp', 'udp', 'imcp'] ? FromPort : -1)",
    "/properties/ToPort" : "($mapVal := $lookup({'1': 'icmp','6': 'tcp','17': 'udp','58': 'icmpv6'}, IpProtocol);$ipProtocol := $mapVal ? $mapVal : $lowercase(IpProtocol);$ipProtocol in ['imcp', 'tcp', 'udp', 'imcp'] ? ToPort : -1)"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:DescribeSecurityGroupRules", "ec2:AuthorizeSecurityGroupIngress" ]
    },
    "update" : {
      "permissions" : [ "ec2:UpdateSecurityGroupRuleDescriptionsIngress" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeSecurityGroupRules", "ec2:RevokeSecurityGroupIngress" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeSecurityGroups", "ec2:DescribeSecurityGroupRules" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeSecurityGroupRules" ]
    }
  }
}