SCHEMA = {
  "typeName" : "AWS::Lightsail::LoadBalancer",
  "description" : "Resource Type definition for AWS::Lightsail::LoadBalancer",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "LoadBalancerName" : {
      "description" : "The name of your load balancer.",
      "type" : "string",
      "pattern" : "\\w[\\w\\-]*\\w"
    },
    "LoadBalancerArn" : {
      "type" : "string"
    },
    "InstancePort" : {
      "description" : "The instance port where you're creating your load balancer.",
      "type" : "integer"
    },
    "IpAddressType" : {
      "description" : "The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.",
      "type" : "string"
    },
    "AttachedInstances" : {
      "description" : "The names of the instances attached to the load balancer.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "HealthCheckPath" : {
      "description" : "The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., \"/\").",
      "type" : "string"
    },
    "SessionStickinessEnabled" : {
      "description" : "Configuration option to enable session stickiness.",
      "type" : "boolean"
    },
    "SessionStickinessLBCookieDurationSeconds" : {
      "description" : "Configuration option to adjust session stickiness cookie duration parameter.",
      "type" : "string"
    },
    "TlsPolicyName" : {
      "description" : "The name of the TLS policy to apply to the load balancer.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "LoadBalancerName", "InstancePort" ],
  "readOnlyProperties" : [ "/properties/LoadBalancerArn" ],
  "primaryIdentifier" : [ "/properties/LoadBalancerName" ],
  "createOnlyProperties" : [ "/properties/LoadBalancerName", "/properties/InstancePort", "/properties/IpAddressType" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateLoadBalancer", "lightsail:GetLoadBalancer", "lightsail:GetLoadBalancers", "lightsail:GetInstance", "lightsail:AttachInstancesToLoadBalancer", "lightsail:DetachInstancesFromLoadBalancer", "lightsail:UpdateLoadBalancerAttribute", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetLoadBalancer", "lightsail:GetLoadBalancers" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetLoadBalancer", "lightsail:GetLoadBalancers", "lightsail:GetInstance", "lightsail:AttachInstancesToLoadBalancer", "lightsail:DetachInstancesFromLoadBalancer", "lightsail:UpdateLoadBalancerAttribute", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteLoadBalancer", "lightsail:GetLoadBalancer", "lightsail:GetLoadBalancers" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetLoadBalancers" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}