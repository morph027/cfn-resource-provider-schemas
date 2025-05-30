SCHEMA = {
  "typeName" : "AWS::EC2::NetworkAclEntry",
  "description" : "Resource Type definition for AWS::EC2::NetworkAclEntry",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "PortRange" : {
      "description" : "The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24). We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18, we modify it to 100.68.0.0/18",
      "$ref" : "#/definitions/PortRange"
    },
    "NetworkAclId" : {
      "description" : "The ID of the network ACL",
      "type" : "string"
    },
    "RuleAction" : {
      "description" : "Indicates whether to allow or deny the traffic that matches the rule",
      "type" : "string"
    },
    "CidrBlock" : {
      "description" : "The IPv4 CIDR range to allow or deny, in CIDR notation (for example, 172.16.0.0/24). Requirement is conditional: You must specify the CidrBlock or Ipv6CidrBlock property",
      "type" : "string"
    },
    "Egress" : {
      "description" : "Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet)",
      "type" : "boolean"
    },
    "RuleNumber" : {
      "description" : "Rule number to assign to the entry, such as 100. ACL entries are processed in ascending order by rule number. Entries can't use the same rule number unless one is an egress rule and the other is an ingress rule",
      "type" : "integer"
    },
    "Ipv6CidrBlock" : {
      "description" : "The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64)",
      "type" : "string"
    },
    "Protocol" : {
      "description" : "The protocol number. A value of \"-1\" means all protocols. If you specify \"-1\" or a protocol number other than \"6\" (TCP), \"17\" (UDP), or \"1\" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code",
      "type" : "integer"
    },
    "Icmp" : {
      "description" : "The Internet Control Message Protocol (ICMP) code and type. Requirement is conditional: Required if specifying 1 (ICMP) for the protocol parameter",
      "$ref" : "#/definitions/Icmp"
    }
  },
  "definitions" : {
    "PortRange" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "From" : {
          "type" : "integer"
        },
        "To" : {
          "type" : "integer"
        }
      }
    },
    "Icmp" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Code" : {
          "type" : "integer"
        },
        "Type" : {
          "type" : "integer"
        }
      }
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "NetworkAclId", "RuleAction", "RuleNumber", "Protocol" ],
  "createOnlyProperties" : [ "/properties/Egress", "/properties/RuleNumber", "/properties/NetworkAclId" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkAclEntry", "ec2:DescribeNetworkAcls" ]
    },
    "update" : {
      "permissions" : [ "ec2:ReplaceNetworkAclEntry", "ec2:DescribeNetworkAcls" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteNetworkAclEntry", "ec2:DescribeNetworkAcls" ]
    }
  }
}