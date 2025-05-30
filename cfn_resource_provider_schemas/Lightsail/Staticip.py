SCHEMA = {
  "typeName" : "AWS::Lightsail::StaticIp",
  "description" : "Resource Type definition for AWS::Lightsail::StaticIp",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : { },
  "properties" : {
    "StaticIpName" : {
      "description" : "The name of the static IP address.",
      "type" : "string"
    },
    "AttachedTo" : {
      "description" : "The instance where the static IP is attached.",
      "type" : "string"
    },
    "IsAttached" : {
      "description" : "A Boolean value indicating whether the static IP is attached.",
      "type" : "boolean"
    },
    "IpAddress" : {
      "description" : "The static IP address.",
      "type" : "string"
    },
    "StaticIpArn" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "StaticIpName" ],
  "readOnlyProperties" : [ "/properties/StaticIpArn", "/properties/IsAttached", "/properties/IpAddress" ],
  "taggable" : True,
  "primaryIdentifier" : [ "/properties/StaticIpName" ],
  "createOnlyProperties" : [ "/properties/StaticIpName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:AllocateStaticIp", "lightsail:AttachStaticIp", "lightsail:DetachStaticIp", "lightsail:GetInstance", "lightsail:GetStaticIp", "lightsail:GetStaticIps" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetStaticIp", "lightsail:GetStaticIps" ]
    },
    "update" : {
      "permissions" : [ "lightsail:AttachStaticIp", "lightsail:DetachStaticIp", "lightsail:GetInstance", "lightsail:GetStaticIp", "lightsail:GetStaticIps" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:GetStaticIp", "lightsail:GetStaticIps", "lightsail:ReleaseStaticIp" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetStaticIps" ]
    }
  }
}