SCHEMA = {
  "tagging" : {
    "permissions" : [ "route53resolver:TagResource", "route53resolver:UntagResource" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False
  },
  "typeName" : "AWS::Route53Resolver::ResolverRule",
  "readOnlyProperties" : [ "/properties/Arn", "/properties/ResolverRuleId" ],
  "description" : "Resource Type definition for AWS::Route53Resolver::ResolverRule",
  "createOnlyProperties" : [ "/properties/RuleType" ],
  "primaryIdentifier" : [ "/properties/ResolverRuleId" ],
  "required" : [ "RuleType" ],
  "conditionalCreateOnlyProperties" : [ "/properties/DomainName" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-route53resolver.git",
  "propertyTransform" : {
    "/properties/DomainName" : "$join([DomainName, \".\"]) $OR DomainName"
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "route53resolver:GetResolverRule", "route53resolver:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "route53resolver:CreateResolverRule", "route53resolver:GetResolverRule", "route53resolver:ListTagsForResource", "route53resolver:TagResource" ]
    },
    "update" : {
      "permissions" : [ "route53resolver:UpdateResolverRule", "route53resolver:GetResolverRule", "route53resolver:ListTagsForResource", "route53resolver:TagResource", "route53resolver:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "route53resolver:ListResolverRules" ]
    },
    "delete" : {
      "permissions" : [ "route53resolver:DeleteResolverRule", "route53resolver:GetResolverRule" ]
    }
  },
  "additionalProperties" : False,
  "definitions" : {
    "TargetAddress" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Ipv6" : {
          "description" : "One IPv6 address that you want to forward DNS queries to. You can specify only IPv6 addresses. ",
          "type" : "string"
        },
        "Ip" : {
          "description" : "One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses. ",
          "type" : "string"
        },
        "Port" : {
          "minLength" : 0,
          "description" : "The port at Ip that you want to forward DNS queries to. ",
          "type" : "string",
          "maxLength" : 65535
        },
        "Protocol" : {
          "description" : "The protocol that you want to use to forward DNS queries. ",
          "type" : "string",
          "enum" : [ "Do53", "DoH" ]
        },
        "ServerNameIndication" : {
          "minLength" : 0,
          "description" : "The SNI of the target name servers for DoH/DoH-FIPS outbound endpoints",
          "type" : "string",
          "maxLength" : 255
        }
      }
    },
    "Tag" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "minLength" : 0,
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 256
        },
        "Key" : {
          "minLength" : 1,
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 128
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "ResolverEndpointId" : {
      "minLength" : 1,
      "description" : "The ID of the endpoint that the rule is associated with.",
      "type" : "string",
      "maxLength" : 64
    },
    "DomainName" : {
      "minLength" : 1,
      "description" : "DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps",
      "type" : "string",
      "maxLength" : 256
    },
    "RuleType" : {
      "description" : "When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.",
      "type" : "string",
      "enum" : [ "FORWARD", "SYSTEM", "RECURSIVE", "DELEGATE" ]
    },
    "ResolverRuleId" : {
      "description" : "The ID of the endpoint that the rule is associated with.",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the resolver rule.",
      "type" : "string"
    },
    "Tags" : {
      "uniqueItems" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "TargetIps" : {
      "uniqueItems" : False,
      "description" : "An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/TargetAddress"
      }
    },
    "Name" : {
      "minLength" : 0,
      "description" : "The name for the Resolver rule",
      "type" : "string",
      "maxLength" : 64
    }
  }
}